from app.constants.profile_steps import PROFILE_STEPS

def get_step_by_state(current_state: str | None):
    for step in PROFILE_STEPS:
        if step["state"].state == current_state:
            return step
        
    return None