import wikipedia


def get_knowledge(query):

    try:

        result = wikipedia.summary(
            query,
            sentences=2,
            auto_suggest=True
        )

        return result

    except wikipedia.exceptions.DisambiguationError as e:

        options = e.options[:3]

        return (
            "There are multiple results for "
            f"{query}. They include: "
            + ", ".join(options)
        )

    except wikipedia.exceptions.PageError:

        return (
            f"Sorry, I could not find information "
            f"about {query}."
        )

    except Exception as e:

        print("Wikipedia error:", e)

        return (
            "Sorry, I could not retrieve "
            "that information."
        )