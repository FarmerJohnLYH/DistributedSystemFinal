import grpc
from concurrent import futures
import time
import queue
import pubsub_pb2
import pubsub_pb2_grpc
from google.protobuf import empty_pb2

class PubSubService(pubsub_pb2_grpc.PubSubServiceServicer):
    def __init__(self):
        self.subscribers = {}
        self.topics = {}

    def Publish(self, request, context):
        # request = (topic,message,sender)
        topic = request.topic
        message = request.message
        if topic in self.topics:
            for subscriber_queue in self.topics[topic]:
                subscriber_queue.put(pubsub_pb2.MessageResponse(message=message))
        return empty_pb2.Empty()

    def Subscribe(self, request, context):
        subscriber_id = request.subscriber_id
        if subscriber_id not in self.subscribers:
            self.subscribers[subscriber_id] = queue.Queue()

        subscriber_queue = self.subscribers[subscriber_id]
        topic = request.topic
        if topic not in self.topics:
            self.topics[topic] = []
        self.topics[topic].append(subscriber_queue)

        while True: #21311223 刘元昊 
            message_response = subscriber_queue.get()  # 获取消息
            yield message_response  # 发送消息给订阅者

    def ListSubscribers(self, request, context):
        return pubsub_pb2.SubscriberList(subscriber_ids=list(self.subscribers.keys()))
    def ListTopics(self, request, context):
        return pubsub_pb2.TopicList(topics=list(self.topics.keys()))
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pubsub_pb2_grpc.add_PubSubServiceServicer_to_server(PubSubService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
