"""
File Name:
message_bus.py

Module:
Swarm Communication Layer

Purpose:
This module enables communication between
multiple agents inside AgentFin-Swarm.

Why Needed?

In a distributed swarm, agents should not
operate in complete isolation.

Example:

Risk Agent
    |
    V
Fraud Agent
    |
    V
Compliance Agent

Messages exchanged may contain:

1. Risk alerts
2. Fraud indicators
3. Compliance warnings
4. Regulatory notifications

Research Contribution:

Introduces a communication mechanism
for inter-agent collaboration which
improves swarm intelligence.

Future Enhancements:

1. RabbitMQ Integration
2. Apache Kafka Integration
3. Event-driven Architecture
4. Real-time Agent Messaging
"""


class MessageBus:
    """
    Central communication layer.
    """

    def __init__(self):

        """
        Initialize message storage.
        """

        self.messages = []

    def publish(
            self,
            sender,
            receiver,
            message):

        """
        Store communication message.

        Parameters:

        sender:
            Agent sending message

        receiver:
            Target agent

        message:
            Communication payload
        """

        self.messages.append({

            "sender": sender,

            "receiver": receiver,

            "message": message
        })

    def get_messages(self):

        """
        Return all messages.

        Returns:
            List of messages
        """

        return self.messages