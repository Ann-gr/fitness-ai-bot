from app.constants.profile_steps import PROFILE_STEPS

def get_step_by_state(current_state: str | None):
    if not current_state:
        return PROFILE_STEPS[0]
    
    for step in PROFILE_STEPS:
        if step["state"].state == current_state:
            return step
        
    return None