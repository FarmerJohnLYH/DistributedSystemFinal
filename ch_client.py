import grpc
import pubsub_pb2
import pubsub_pb2_grpc
from google.protobuf import empty_pb2
import time
import threading

def publish_message(stub, topic, content, sender_id):
    message = pubsub_pb2.Message(content=content, sender_id=sender_id)
    request = pubsub_pb2.PublishRequest(sender_id=sender_id, topic=topic, message=message)
    # 发布消息
    stub.Publish(request)

def subscribe_to_messages(stub, subscriber_id, topic):
    request = pubsub_pb2.SubscribeRequest(subscriber_id=subscriber_id, topic=topic)
    for response in stub.Subscribe(request):
        message = response.message
        print(f"收到来自 {message.sender_id} 的消息: {message.content}")

def list_subscribers(stub):
    response = stub.ListSubscribers(empty_pb2.Empty())
    print("当前订阅者:", response.subscriber_ids)
    # 显示所有被订阅的主题 
    response = stub.ListTopics(empty_pb2.Empty())
    print("当前主题:", response.topics)
    

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pubsub_pb2_grpc.PubSubServiceStub(channel)

        while True:
            option = input("输入 'p' 发布消息，'s' 订阅消息，'l' 列出订阅者，'q' 退出: ").strip()
            if option == 'p':
                topic = input("输入主题: ")
                content = input("输入消息内容: ")
                sender_id = input("输入发送者 ID: ")
                publish_message(stub, topic, content, sender_id)
            elif option == 's':
                subscriber_id = input("输入订阅者 ID: ")
                topic = input('输入主题:')
                threading.Thread(target=subscribe_to_messages, args=(stub, subscriber_id, topic)).start()
            elif option == 'l':
                list_subscribers(stub)
            elif option == 'q':
                break
            else:
                print("无效选项")

if __name__ == '__main__':
    run()
