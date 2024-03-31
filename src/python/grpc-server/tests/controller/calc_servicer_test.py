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
    print(calc_service.methods_by_name)
    rpc = real_time_server.invoke_unary_unary(
        calc_service.methods_by_name["Add"],
        (),
        calc_pb2.AddRequest(x=1, y=2),
        None,
    )

    response, trailing_metadata, code, details = rpc.termination()
    print(response.result)
    assert calc_pb2.AddResponse(result=3) == response
    assert code == grpc.StatusCode.OK
