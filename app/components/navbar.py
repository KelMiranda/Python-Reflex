import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Kelvin Miranda",
            height="40px"
        ),
        position="sticky",
        padding="16px"

    )