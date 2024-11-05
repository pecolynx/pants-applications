poetry_requirements(
    name="poetry",
    resolve="lib_pydantic_v1",
)

python_sources(
    name="src",
    resolve="lib_pydantic_v1",
    sources=["lib_pydantic_v1/**/*.py"],
)


python_tests(name="tests", resolve="lib_pydantic_v1", sources=["tests/**/*_test.py"], dependencies=[])

# dep_test
poetry_requirements(
    name="dep_test_poetry",
    resolve="dep_test",
    
)
python_sources(
    name="dep_test_src",
    resolve="dep_test",
    sources=["lib_pydantic_v1/**/*.py"],
)
