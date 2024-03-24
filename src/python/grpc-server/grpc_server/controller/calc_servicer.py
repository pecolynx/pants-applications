import grpc
from calc.v1 import calc_pb2, calc_pb2_grpc


class CalcServicer(calc_pb2_grpc.CalcServicer):
    def Add(
        self, request: calc_pb2.AddRequest, context: grpc.ServicerContext
    ) -> calc_pb2.AddResponse:
        return calc_pb2.AddResponse(result=request.a + request.b)
