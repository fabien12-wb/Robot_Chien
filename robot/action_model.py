from typing import Literal

from pydantic import BaseModel, Field, ValidationError


class RobotAction(BaseModel):
    action: Literal[
        "stand_up",
        "stand_down",
        "forward",
        "backward",
        "turn_left",
        "turn_right",
        "spin_left",
        "spin_right",
        "stop"
    ]

    duration: float = Field(
        default=0,
        ge=0,
        le=3
    )


def validate_actions(raw_actions):
    validated_actions = []

    for item in raw_actions:
        try:
            action = RobotAction.model_validate(item)

            # Les actions qui ne sont pas des déplacements
            # n'ont pas besoin de durée.
            if action.action in [
                "stand_up",
                "stand_down",
                "stop"
            ]:
                action.duration = 0

            validated_actions.append(
                action.model_dump()
            )

        except ValidationError as error:
            print("Action invalide ignorée :", item)
            print(error)

    return validated_actions