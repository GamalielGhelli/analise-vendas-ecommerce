"""Exibe as versões do ambiente usado no desenvolvimento do projeto."""

from watermark import watermark


def main():
    print(
        watermark(
            python=True,
            packages="numpy,pandas,matplotlib,seaborn,watermark",
            current_date=True,
            author="Gamaliel Ghelli"
        )
    )

if __name__ == "__main__":
    main()
