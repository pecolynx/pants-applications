poetry_requirements(
    name="poetry",
    resolve="grpc_server",
)

python_sources(
    name="src",
    resolve="grpc_server",
    sources=["grpc_server/**/*.py"],
    # dependencies=[
    #     ":poetry",
    #     # "//protos:helloworld/v1/grpc_server#django",
    # ]
)

pex_binary(
    name="grpc_server",
    resolve="grpc_server",
    interpreter_constraints=["CPython>=3.10"],
    entry_point="grpc_server/main.py",
)

python_tests(
    name="tests",
    resolve="pytest",
    sources=["tests/**/*_test.py"],
    dependencies=[
    ]
)

docker_image(
    name="docker",
    image_tags=["{build_args.GIT_COMMIT}"],
    repository="grpc_server",
)
