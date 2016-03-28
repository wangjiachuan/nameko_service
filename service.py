from nameko.events import event_handler
import mandrill
from jsonschema import validate, exceptions


class Mailer(object):
    """ This is a main service class accepting messages payloads from payments service.

        TODO:
        - Remove hard dependency on Mandrill and allow for swapping for different implementations.
            Potentially use concept of Nameko Dependencies.
        - Move Madrill API Key to environment variable
    """
    name = "mailer"

    mailer_provider = mandrill.Mandrill("8eZMbUkC5HFrN79k1JwHBg")


    @event_handler("payments", "payment_received")
    def handle_event(self, payload):

        """
        Args:
            payload (object): all necessary data for sending email client
        """

        print "Payload received", payload

        results = {
            "success": False,
            "errors": []
        }

        if not validate_payload(payload):
            results["success"] = False
            results["errors"].append("Invalid Payload")
            return results

        try:
            message_text = construct_message_text(payload)
            message = construct_message(message_text, payload)
            self.mailer_provider.messages.send(message=message)

            results["success"] = True
            return results

        except mandrill.Error, e:
            results["success"] = False
            results["errors"].append("A mandrill error occurred: %s - %s" % (e.__class__, e))
