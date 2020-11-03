# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rock_paper_scissors_pb2 as rock__paper__scissors__pb2


class RockPaperScissorsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.JoinGame = channel.unary_unary(
                '/RockPaperScissors/JoinGame',
                request_serializer=rock__paper__scissors__pb2.Gamer.SerializeToString,
                response_deserializer=rock__paper__scissors__pb2.GamerList.FromString,
                )
        self.StartRound = channel.unary_unary(
                '/RockPaperScissors/StartRound',
                request_serializer=rock__paper__scissors__pb2.Gamer.SerializeToString,
                response_deserializer=rock__paper__scissors__pb2.GameRound.FromString,
                )
        self.PlayHand = channel.unary_unary(
                '/RockPaperScissors/PlayHand',
                request_serializer=rock__paper__scissors__pb2.PlayerHand.SerializeToString,
                response_deserializer=rock__paper__scissors__pb2.GameResult.FromString,
                )


class RockPaperScissorsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def JoinGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartRound(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlayHand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RockPaperScissorsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'JoinGame': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinGame,
                    request_deserializer=rock__paper__scissors__pb2.Gamer.FromString,
                    response_serializer=rock__paper__scissors__pb2.GamerList.SerializeToString,
            ),
            'StartRound': grpc.unary_unary_rpc_method_handler(
                    servicer.StartRound,
                    request_deserializer=rock__paper__scissors__pb2.Gamer.FromString,
                    response_serializer=rock__paper__scissors__pb2.GameRound.SerializeToString,
            ),
            'PlayHand': grpc.unary_unary_rpc_method_handler(
                    servicer.PlayHand,
                    request_deserializer=rock__paper__scissors__pb2.PlayerHand.FromString,
                    response_serializer=rock__paper__scissors__pb2.GameResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RockPaperScissors', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RockPaperScissors(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def JoinGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RockPaperScissors/JoinGame',
            rock__paper__scissors__pb2.Gamer.SerializeToString,
            rock__paper__scissors__pb2.GamerList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartRound(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RockPaperScissors/StartRound',
            rock__paper__scissors__pb2.Gamer.SerializeToString,
            rock__paper__scissors__pb2.GameRound.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlayHand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RockPaperScissors/PlayHand',
            rock__paper__scissors__pb2.PlayerHand.SerializeToString,
            rock__paper__scissors__pb2.GameResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
