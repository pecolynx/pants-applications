poetry_requirements(
    name="poetry",
    resolve="sqs_consumer",
    module_mapping={
        "amazon-sqs-extended-client": ["sqs_extended_client"],
    },
)

python_sources(
    name="src",
    resolve="sqs_consumer",
    sources=["sqs_consumer/**/*.py"],
)

pex_binary(
    name="sqs_consumer",
    resolve="sqs_consumer",
    interpreter_constraints=["CPython>=3.10"],
    entry_point="sqs_consumer/main.py",
)

python_tests(
    name="tests",
    resolve="sqs_consumer",
    sources=["tests/**/*_test.py"],
    dependencies=[
        ":poetry#moto",
        # "3rdparty/python:pytest#pytest",
    ],
)

docker_image(
    name="docker",
    image_tags=["{build_args.GIT_COMMIT}"],
    repository="sqs_consumer",
)
