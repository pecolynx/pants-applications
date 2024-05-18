import grpc
import grpc_testing
import pytest
from calc.v1 import calc_pb2
from grpc_server.controller.calc_servicer import CalcServicer


def test_a():
    assert 1 == 1


@pytest.fixture()
def real_time_server():
    real_time = grpc_testing.strict_real_time()
    # self._fake_time = grpc_testing.strict_fake_time(time.time())
    servicer = CalcServicer()
    calc_service = calc_pb2.DESCRIPTOR.services_by_name["Calc"]
    descriptors_to_servicers = {
        calc_service: servicer,
    }
    return grpc_testing.server_from_dictionary(descriptors_to_servicers, real_time)
    # self._fake_time_server = grpc_testing.server_from_dictionary(
    #     descriptors_to_servicers, self._fake_time
    # )


def test_successful_unary_unary(real_time_server):
    calc_service = calc_pb2.DESCRIPTOR.services_by_name["Calc"]
    # print(calc_service.methods_by_name)
    rpc = real_time_server.invoke_unary_unary(
        calc_service.methods_by_name["Add"],
        (),
        calc_pb2.AddRequest(x=1, y=2),
        None,
    )

    response, trailing_metadata, code, details = rpc.termination()

    assert response == calc_pb2.AddResponse(result=3)
    assert code == grpc.StatusCode.OK


def test_successful_unary_stream(real_time_server):
    calc_service = calc_pb2.DESCRIPTOR.services_by_name["Calc"]
    # print(calc_service.methods_by_name)
    rpc = real_time_server.invoke_unary_stream(
        calc_service.methods_by_name["Divisors"],
        (),
        calc_pb2.DivisorsRequest(x=12),
        None,
    )

    # initial_metadata = rpc.initial_metadata()

    responses = [rpc.take_response() for _ in range(6)]
    # print(initial_metadata)

    trailing_metadata, code, details = rpc.termination()

    # print(trailing_metadata)
    # print(details)

    assert responses[0] == calc_pb2.DivisorsResponse(result=1)
    assert responses[1] == calc_pb2.DivisorsResponse(result=2)
    assert responses[2] == calc_pb2.DivisorsResponse(result=3)
    assert responses[3] == calc_pb2.DivisorsResponse(result=4)
    assert responses[4] == calc_pb2.DivisorsResponse(result=6)
    assert responses[5] == calc_pb2.DivisorsResponse(result=12)
    assert code == grpc.StatusCode.OK


def test_successful_stream_unary(real_time_server):
    calc_service = calc_pb2.DESCRIPTOR.services_by_name["Calc"]
    # print(calc_service.methods_by_name)
    rpc = real_time_server.invoke_stream_unary(
        calc_service.methods_by_name["Sum"],
        (),
        None,
    )
    rpc.send_request(calc_pb2.SumRequest(x=1))
    rpc.send_request(calc_pb2.SumRequest(x=2))
    rpc.send_request(calc_pb2.SumRequest(x=3))
    rpc.requests_closed()

    # initial_metadata = rpc.initial_metadata()
    # print(initial_metadata)

    response, trailing_metadata, code, details = rpc.termination()
    # print(trailing_metadata)
    # print(details)
    # print(response.result)
    assert response == calc_pb2.SumResponse(result=6)
    assert code == grpc.StatusCode.OK
