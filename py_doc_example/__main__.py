from py_doc_example.uff_module import UFFClass, print_greetings


def run() -> int:
    arthur = UFFClass("Arthur")
    print_greetings(arthur)
    return 0


if __name__ == "__main__":
    run()
