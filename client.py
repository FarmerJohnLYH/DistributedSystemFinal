import grpc
import pubsub_pb2
import pubsub_pb2_grpc
from google.protobuf import empty_pb2
import time
import threading

def publish_message(stub, topic, content, sender_id):
    message = pubsub_pb2.Message(content=content, sender_id=sender_id)
    request = pubsub_pb2.PublishRequest(sender_id=sender_id, topic=topic, message=message)
    # 
    stub.Publish(request)

def subscribe_to_messages(stub, subscriber_id,topic):
    request = pubsub_pb2.SubscribeRequest(subscriber_id=subscriber_id,topic=topic)
    for response in stub.Subscribe(request):
        message = response.message
        print(f"Received message from {message.sender_id}: {message.content}")

def list_subscribers(stub):
    response = stub.ListSubscribers(empty_pb2.Empty())
    print("Current subscribers:", response.subscriber_ids)
    # 显示所有被订阅的主题 
    response = stub.ListTopics(empty_pb2.Empty())
    print("Current topics:", response.topic)
    

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pubsub_pb2_grpc.PubSubServiceStub(channel)

        while True:
            option = input("Enter 'p' to publish, 's' to subscribe, 'l' to list subscribers, 'q' to quit: ").strip()
            if option == 'p':
                topic = input("Enter topic: ")
                content = input("Enter message content: ")
                sender_id = input("Enter sender ID: ")
                publish_message(stub, topic, content, sender_id)
            elif option == 's':
                subscriber_id = input("Enter subscriber ID: ")
                topic = input('Enter topic:')
                threading.Thread(target=subscribe_to_messages, args=(stub, subscriber_id,topic)).start()
            elif option == 'l':
                list_subscribers(stub)
            elif option == 'q':
                break
            else:
                print("Invalid option")

if __name__ == '__main__':
    run()

