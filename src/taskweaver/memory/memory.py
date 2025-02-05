from taskweaver.memory.conversation import Conversation
from taskweaver.memory.round import Round
from taskweaver.memory.type_vars import RoleName

class Memory:
    """
    Memory is used to store all the conversations in the system,
    which should be initialized when creating a session.
    """

    def __init__(self, session_id: str) -> None:
        self.session_id = session_id
        self.conversation = Conversation.init()

    def create_round(self, user_query: str) -> Round:
        """Create a round with the given query."""
        round = Round.create(user_query=user_query)
        self.conversation.add_round(round)
        return round

    def get_role_rounds(self, role: RoleName, include_failure_rounds: bool = False) -> List[Round]:
        """Get all the rounds of the given role in the memory."""
        rounds_from_role: List[Round] = []
        for round in self.conversation.rounds:
            if round.state == "failed" and not include_failure_rounds:
                continue
            if any(post.send_from == role or post.send_to == role for post in round.post_list):
                rounds_from_role.append(round)
        return rounds_from_role