from concurrent import futures

import grpc
from calc.v1 import calc_pb2_grpc
from grpc_server.controller.calc_servicer import CalcServicer
from helloworld.v1 import helloworld_pb2, helloworld_pb2_grpc


class GreeterServicer(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(
        self, request: helloworld_pb2.HelloRequest, context: grpc.ServicerContext
    ) -> helloworld_pb2.HelloReply:
        return helloworld_pb2.HelloReply(message=f"Hello, {request.name}")


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

helloworld_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

calc_pb2_grpc.add_CalcServicer_to_server(CalcServicer(), server)

server.add_insecure_port("[::]:50052")
server.start()
print("gRPC server listening at :50052")
server.wait_for_termination()
