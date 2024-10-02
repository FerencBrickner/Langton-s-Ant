import turtle


def initialize_turtle(*, background_color: str = "gray") -> None:
    turtle.bgcolor(background_color)


def initialize_ant(
    *,
    ant_speed: int | float = 0,
    ant_shape: str = "square",
    ant_size: int | float = 0.5,
) -> object:
    initialize_turtle()
    ant = turtle.Turtle()
    ant.speed(ant_speed)
    ant.shape(ant_shape)
    ant.shapesize(ant_size)
    return ant


def set_color_of_block(
    *, coordinate_color_pairs: dict[tuple[int, int], str], color: str, ant: object
) -> None:
    ant.fillcolor(color)
    ant_coordinates: tuple[int, int] = obtain_ant_coordinates(ant)
    coordinate_color_pairs[ant_coordinates] = color


def obtain_ant_coordinates(ant: object) -> tuple[int, int]:
    first_coordinate: int = round(ant.xcor())
    second_coordinate: int = round(ant.ycor())
    return first_coordinate, second_coordinate


def compute_and_draw_langtons_ant(
    *,
    step_count: int = 11_000,
    ant_step_size: int | float = 10,
    coordinate_color_pairs: dict[tuple[int, int], str] = dict(),
    color_1: str = "white",
    color_2: str = "blue",
    angle: int | float = 90,
    ant: object = initialize_ant(),
) -> None:
    assert color_1 != color_2
    for _ in range(step_count):
        current_ant_position: tuple[int, int] = obtain_ant_coordinates(ant)
        if (
            current_ant_position not in coordinate_color_pairs
            or coordinate_color_pairs[current_ant_position] == color_1
        ):
            set_color_of_block(
                coordinate_color_pairs=coordinate_color_pairs, color=color_2, ant=ant
            )
            ant.right(angle)
        else:
            set_color_of_block(
                coordinate_color_pairs=coordinate_color_pairs, color=color_1, ant=ant
            )
            ant.left(angle)
        ant.stamp()
        ant.forward(ant_step_size)


def main(*args, **kwargs) -> None:
    """
    Compute and draw Langton's ant.
    https://en.wikipedia.org/wiki/Langton%27s_ant
    """
    compute_and_draw_langtons_ant()
    turtle.done()


if __name__ == "__main__":
    main()
