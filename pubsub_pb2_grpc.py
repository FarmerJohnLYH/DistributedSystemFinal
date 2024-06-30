# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import pubsub_pb2 as pubsub__pb2


class PubSubServiceStub(object):
    """发布-订阅服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Publish = channel.unary_unary(
                '/pubsub.PubSubService/Publish',
                request_serializer=pubsub__pb2.PublishRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/pubsub.PubSubService/Subscribe',
                request_serializer=pubsub__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=pubsub__pb2.MessageResponse.FromString,
                )
        self.ListSubscribers = channel.unary_unary(
                '/pubsub.PubSubService/ListSubscribers',
                request_serializer=pubsub__pb2.Empty.SerializeToString,
                response_deserializer=pubsub__pb2.SubscriberList.FromString,
                )
        self.ListTopics = channel.unary_unary(
                '/pubsub.PubSubService/ListTopics',
                request_serializer=pubsub__pb2.Empty.SerializeToString,
                response_deserializer=pubsub__pb2.TopicList.FromString,
                )


class PubSubServiceServicer(object):
    """发布-订阅服务
    """

    def Publish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSubscribers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTopics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PubSubServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=pubsub__pb2.PublishRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=pubsub__pb2.SubscribeRequest.FromString,
                    response_serializer=pubsub__pb2.MessageResponse.SerializeToString,
            ),
            'ListSubscribers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSubscribers,
                    request_deserializer=pubsub__pb2.Empty.FromString,
                    response_serializer=pubsub__pb2.SubscriberList.SerializeToString,
            ),
            'ListTopics': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTopics,
                    request_deserializer=pubsub__pb2.Empty.FromString,
                    response_serializer=pubsub__pb2.TopicList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pubsub.PubSubService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PubSubService(object):
    """发布-订阅服务
    """

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pubsub.PubSubService/Publish',
            pubsub__pb2.PublishRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pubsub.PubSubService/Subscribe',
            pubsub__pb2.SubscribeRequest.SerializeToString,
            pubsub__pb2.MessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSubscribers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pubsub.PubSubService/ListSubscribers',
            pubsub__pb2.Empty.SerializeToString,
            pubsub__pb2.SubscriberList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListTopics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pubsub.PubSubService/ListTopics',
            pubsub__pb2.Empty.SerializeToString,
            pubsub__pb2.TopicList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
