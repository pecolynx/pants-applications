from ddtrace import tracer

trace = tracer.trace("main")
trace.set_tag("env", "dev")
trace.finish()
