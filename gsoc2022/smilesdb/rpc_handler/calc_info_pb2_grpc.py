# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calc_info_pb2 as calc__info__pb2


class CalcInfoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateCalcinfo = channel.unary_unary(
                '/calcInfo.CalcInfoService/CreateCalcinfo',
                request_serializer=calc__info__pb2.CreateInfoRequest.SerializeToString,
                response_deserializer=calc__info__pb2.CreateInfoResponse.FromString,
                )
        self.ReadCalcInfo = channel.unary_unary(
                '/calcInfo.CalcInfoService/ReadCalcInfo',
                request_serializer=calc__info__pb2.ReadInfoRequest.SerializeToString,
                response_deserializer=calc__info__pb2.ReadInfoResponse.FromString,
                )
        self.UpdateCalcInfo = channel.unary_unary(
                '/calcInfo.CalcInfoService/UpdateCalcInfo',
                request_serializer=calc__info__pb2.UpdateInfoRequest.SerializeToString,
                response_deserializer=calc__info__pb2.UpdateInfoResponse.FromString,
                )
        self.DeleteCalcInfo = channel.unary_unary(
                '/calcInfo.CalcInfoService/DeleteCalcInfo',
                request_serializer=calc__info__pb2.DeleteInfoRequest.SerializeToString,
                response_deserializer=calc__info__pb2.DeleteInfoResponse.FromString,
                )
        self.ListCalcInfo = channel.unary_stream(
                '/calcInfo.CalcInfoService/ListCalcInfo',
                request_serializer=calc__info__pb2.ListInfoRequest.SerializeToString,
                response_deserializer=calc__info__pb2.ListInfoResponse.FromString,
                )


class CalcInfoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateCalcinfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadCalcInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCalcInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCalcInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCalcInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalcInfoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateCalcinfo': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCalcinfo,
                    request_deserializer=calc__info__pb2.CreateInfoRequest.FromString,
                    response_serializer=calc__info__pb2.CreateInfoResponse.SerializeToString,
            ),
            'ReadCalcInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadCalcInfo,
                    request_deserializer=calc__info__pb2.ReadInfoRequest.FromString,
                    response_serializer=calc__info__pb2.ReadInfoResponse.SerializeToString,
            ),
            'UpdateCalcInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCalcInfo,
                    request_deserializer=calc__info__pb2.UpdateInfoRequest.FromString,
                    response_serializer=calc__info__pb2.UpdateInfoResponse.SerializeToString,
            ),
            'DeleteCalcInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCalcInfo,
                    request_deserializer=calc__info__pb2.DeleteInfoRequest.FromString,
                    response_serializer=calc__info__pb2.DeleteInfoResponse.SerializeToString,
            ),
            'ListCalcInfo': grpc.unary_stream_rpc_method_handler(
                    servicer.ListCalcInfo,
                    request_deserializer=calc__info__pb2.ListInfoRequest.FromString,
                    response_serializer=calc__info__pb2.ListInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'calcInfo.CalcInfoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CalcInfoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateCalcinfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calcInfo.CalcInfoService/CreateCalcinfo',
            calc__info__pb2.CreateInfoRequest.SerializeToString,
            calc__info__pb2.CreateInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadCalcInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calcInfo.CalcInfoService/ReadCalcInfo',
            calc__info__pb2.ReadInfoRequest.SerializeToString,
            calc__info__pb2.ReadInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCalcInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calcInfo.CalcInfoService/UpdateCalcInfo',
            calc__info__pb2.UpdateInfoRequest.SerializeToString,
            calc__info__pb2.UpdateInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCalcInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calcInfo.CalcInfoService/DeleteCalcInfo',
            calc__info__pb2.DeleteInfoRequest.SerializeToString,
            calc__info__pb2.DeleteInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCalcInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/calcInfo.CalcInfoService/ListCalcInfo',
            calc__info__pb2.ListInfoRequest.SerializeToString,
            calc__info__pb2.ListInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
