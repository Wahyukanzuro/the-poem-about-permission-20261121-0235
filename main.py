import os

POEM = """I gave you my name to carry into the room,
my yes, my no, my key.
You knocked. They opened. And when you came back,
you laid it in my hand — still warm, still mine."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
