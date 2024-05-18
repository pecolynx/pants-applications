from typing import Generator, Iterator

import grpc
from calc.v1 import calc_pb2, calc_pb2_grpc


class CalcServicer(calc_pb2_grpc.CalcServicer):
    def Add(
        self, request: calc_pb2.AddRequest, context: grpc.ServicerContext
    ) -> calc_pb2.AddResponse:
        return calc_pb2.AddResponse(result=request.x + request.y)

    def Sum(
        self, request_iterator: Iterator[calc_pb2.SumRequest], context: grpc.ServicerContext
    ) -> calc_pb2.AddResponse:
        result = 0
        for request in request_iterator:
            result += request.x
        return calc_pb2.SumResponse(result=result)

    def Divisors(
        self, request: calc_pb2.DivisorsRequest, context: grpc.ServicerContext
    ) -> Generator[calc_pb2.DivisorsResponse, None, None]:
        for i in range(1, request.x + 1):
            if request.x % i == 0:
                yield calc_pb2.DivisorsResponse(result=i)
