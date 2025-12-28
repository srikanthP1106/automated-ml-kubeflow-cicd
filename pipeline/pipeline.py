from kfp import dsl, compiler


@dsl.component(base_image="python:3.10")

def preprocess():
    print("Preprocessing data")


@dsl.component(base_image="python:3.10")

def train():
    print("Training model")


@dsl.component(base_image="python:3.10")

def evaluate():
    print("Evaluating model")


@dsl.pipeline(
    name="Automated ML CI/CD Pipeline",
    description="Preprocess -> Train -> Evaluate"

)
def ml_pipeline():
    p = preprocess()
    t = train()
    e = evaluate()

    t.after(p)
    e.after(t)


if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=ml_pipeline,
        package_path="pipeline.yaml"
    )
