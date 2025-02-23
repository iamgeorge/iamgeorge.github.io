import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.translate.meteor_score import meteor_score

# Ensure you have the necessary NLTK corpora
nltk.download('wordnet')


def calculate_scores(reference_texts, hypothesis):
    """
    Calculates BLEU and METEOR scores for a given translation.

    :param reference_texts: List of reference translations (each as a list of words).
    :param hypothesis: The translated text to evaluate (as a list of words).
    :return: BLEU and METEOR scores
    """
    # Convert reference texts into tokenized lists
    reference_tokenized = [ref.split() for ref in reference_texts]
    hypothesis_tokenized = hypothesis.split()

    # Calculate BLEU Score
    # Smoothing to avoid zero BLEU for short sentences
    smoothing = SmoothingFunction().method1
    bleu = sentence_bleu(reference_tokenized,
                         hypothesis_tokenized, smoothing_function=smoothing)

    # Calculate METEOR Score
    meteor = meteor_score(reference_tokenized, hypothesis_tokenized)

    return bleu, meteor


# Example Usage:
if __name__ == "__main__":
    references = [
        """
The Joint Inspection Unit produced six products in 2024: three reports on
system-wide reviews, one report on management and administration reviews of a
single organization, and two notes. The Unit began 2024 with nine reviews in its
workplan, comprising three reviews carried over from 2023 and six reviews in its
programme of work for 2024. The status of the implementation of the workplan for
2024 is included in annex I to the present report, and the summaries of the reviews
that were completed are set out in section A below.
2. In mid-2024, the Unit added a review of the ombudsman and mediation function
in United Nations system organizations to its programme of work, which is part of
the JIU cluster of reports addressing oversight, integrity and accountability. With the
review, the Unit complements its cycle of updating or complementing past reviews of
the United Nations system1

that fall under the cluster. Building on the findings of the
2015 review of organizational ombudsman services, and complementing the 2023
review of internal pre-tribunal appeal mechanisms, the current review provides an
examination of the current state of the function within the organizations and its
evolving role in informal conflict resolution and in fostering a harmonious workplace
environment. It provides an assessment of the adequacy of the organizational set-up
of the function and its mandates and main areas of responsibility while providing an
evaluation of the progress made in implementing recommendations from the previous
report and new developments that have a bearing on the function. Based on its
findings, and through the highlighting of good practices, the review will include
recommendations to enhance the coherence, efficiency and effectiveness of the
ombudsman and mediation function. The findings will be presented under a dedicated
agenda item of the General Assembly at its eighty-first session.
3. In the sections that follow the summaries of the completed reports and notes in
the present chapter, the Unit provides an overview of other significant activities that
were undertaken in 2024, including the Unit’s engagement with executive heads of
participating organizations, oversight entities, and legislative organs and governing
bodies. The present chapter also includes the Unit’s midpoint assessment of its

strategic framework and the progress made on the implementation of its self-
assessment recommendations, and a brief update on the Unit’s resources and action

taken to replace the tracking system for recommendations issued to participating
organizations.


"""

    ]

    original = """
1. In 2024, the Joint Inspection Unit (JIU) produced six outputs: three reports on system-wide reviews, one report on the management and administration review of a single entity, and two notes. At the beginning of 2024, the JIU work plan included nine reviews, comprising three carried over from 2023 and six added to the 2024 work program. The status of the 2024 work plan is presented in Annex I of this report, and the completed reviews are summarized in Section A below.

2. In mid-2024, the JIU added to its work program a review of the ombudsman function and mediation services within United Nations entities. This review is part of the JIU’s series of reports on oversight, integrity, and accountability. With this review, the JIU completes its cycle of updating or supplementing previous reviews of the United Nations system that fall within this category of reports. Building on the findings of the 2015 review of ombudsman services in UN system organizations and complementing the 2023 review of internal pre-litigation grievance mechanisms, the ongoing review examines the current state of the function within entities and the evolution of its role in resolving disputes amicably and promoting a harmonious work environment. It provides an assessment of the effectiveness of the institutional framework of the function, its mandates, and key areas of responsibility, as well as an evaluation of the implementation of recommendations from the previous report and any new developments that may have affected the function. Based on its findings and highlighting best practices, the review will propose recommendations to enhance the coherence, efficiency, and effectiveness of the ombudsman function and mediation services. The results will be presented to the General Assembly under an agenda item at its eighty-first session.

3. In the sections following the summaries of completed reports and notes in this chapter, the JIU provides an overview of other key activities carried out in 2024, including its dialogue with the heads of secretariats of participating entities, oversight bodies, deliberative bodies, and governing bodies. This chapter also includes the mid-term assessment of the JIU’s strategic framework and the follow-up on recommendations from its self-evaluation, as well as an update on JIU resources and measures taken to replace the system for tracking recommendations addressed to participating entities.

"""

    grammar = """

In 2024, the Joint Inspection Unit (JIU) produced six outputs: three reports on system-wide reviews, one report on the review of the management and administration of a single entity, and two notes. At the beginning of 2024, the JIU work plan included nine reviews, comprising three carried over from 2023 and six newly added to the 2024 work program. The status of the 2024 work plan is presented in Annex I of this report, with the completed reviews summarized in Section A below.

In mid-2024, the JIU added a review of the ombudsman function and mediation services within United Nations entities to its work program. This review is part of the JIU’s series of reports on oversight, integrity, and accountability. With this addition, the JIU completes its cycle of updating or supplementing previous reviews of the United Nations system that fall within this category of reports. Building on the findings of the 2015 review of ombudsman services in UN system organizations and complementing the 2023 review of internal pre-litigation grievance mechanisms, the ongoing review examines the current state of the function within entities and its evolving role in resolving disputes amicably and fostering a harmonious work environment. It assesses the effectiveness of the function’s institutional framework, mandates, and key areas of responsibility, while also evaluating the implementation of recommendations from the previous report and any new developments affecting the function. Based on its findings and best practices, the review will propose recommendations to improve the coherence, efficiency, and effectiveness of the ombudsman function and mediation services. The results will be presented to the General Assembly as part of an agenda item at its eighty-first session.

Following the summaries of completed reports and notes in this chapter, the JIU provides an overview of other key activities carried out in 2024, including dialogues with the heads of secretariats of participating entities, oversight bodies, deliberative bodies, and governing bodies. This chapter also includes a mid-term assessment of the JIU’s strategic framework, a follow-up on recommendations from its self-evaluation, and an update on JIU resources and measures taken to replace the system for tracking recommendations addressed to participating entities.



"""

accuracy = """ 

In 2024, the Joint Inspection Unit (JIU) produced six outputs: three reports on system-wide reviews, one report on the management and administration of a single entity, and two notes. At the beginning of 2024, the JIU work plan included nine reviews, comprising three carried over from 2023 and six newly added for 2024. The status of the 2024 work plan is presented in Annex I of this report, and the completed reviews are summarized in Section A below.

In mid-2024, the JIU added to its work program a review of the ombudsman function and mediation services within United Nations entities, as part of its series of reports on oversight, integrity, and accountability. With this review, the JIU completes its cycle of updating or supplementing previous reviews of the United Nations system within this category. Building on the findings of the 2015 review of ombudsman services in UN system organizations and complementing the 2023 review of internal pre-litigation grievance mechanisms, the ongoing review examines the current state of the function within entities and the evolution of its role in the amicable resolution of disputes and the promotion of a harmonious work environment. It provides an assessment of the effectiveness of the institutional framework governing this function, its mandates, and key areas of responsibility, as well as an evaluation of the implementation of recommendations from the previous report and any new developments that may have impacted the function. Based on its findings and highlighting best practices, the review will propose recommendations to improve the coherence, efficiency, and effectiveness of the ombudsman function and mediation services. The results will be presented to the General Assembly under an agenda item at its eighty-first session.

Following the summaries of completed reports and notes in this chapter, the JIU provides an overview of other key activities carried out in 2024, including its dialogue with the heads of secretariats of participating entities, oversight bodies, deliberative bodies, and governing bodies. This chapter also includes the mid-term assessment of the JIU’s strategic framework and the follow-up on recommendations from its self-evaluation, as well as an update on JIU resources and measures taken to replace the system for tracking recommendations addressed to participating entities.




"""

context = """

In 2024, the Joint Inspection Unit (JIU) produced six key outputs: three reports on system-wide reviews, one report on the management and administration of a single entity, and two briefing notes. At the start of 2024, the JIU work plan included nine reviews—three carried over from 2023 and six newly added for 2024. The status of the 2024 work plan is detailed in Annex I of this report, while summaries of completed reviews can be found in Section A below.

In mid-2024, the JIU incorporated a review of the ombudsman function and mediation services within United Nations entities into its work program. This review is part of the JIU’s series of reports on oversight, integrity, and accountability. With this addition, the JIU completes its cycle of updates and enhancements to previous reviews concerning this category of reports within the UN system. Building on the findings of the 2015 review of ombudsman services across UN system organizations, and complementing the 2023 review of internal pre-litigation grievance mechanisms, the current review examines the present state of the ombudsman function within UN entities. It also explores how the role has evolved in facilitating amicable dispute resolution and fostering a positive and constructive work environment. This assessment evaluates the institutional framework governing the function, its mandate, and its core areas of responsibility. Additionally, it reviews the implementation of recommendations from the previous report, along with new developments that may have influenced the function. Drawing from its findings and showcasing best practices, the review will present recommendations aimed at improving the coherence, efficiency, and effectiveness of the ombudsman function and mediation services. The findings will be submitted to the General Assembly as part of the agenda for its eighty-first session.

Following the summaries of completed reports and notes in this chapter, the JIU provides an overview of other key activities undertaken in 2024. These include ongoing dialogues with heads of secretariats of participating entities, oversight bodies, deliberative bodies, and governing bodies. This chapter also presents a mid-term assessment of the JIU’s strategic framework, a follow-up on the implementation of recommendations from its self-evaluation, and an update on JIU resources, including measures taken to replace the system for tracking recommendations addressed to participating entities.


"""


consistency = """

In 2024, the Joint Inspection Unit (JIU) produced six outputs: three reports on system-wide reviews, one report on the management and administration review of a single entity, and two notes. At the beginning of 2024, the JIU work plan included nine reviews, comprising three carried over from 2023 and six newly added for 2024. The status of the 2024 work plan is presented in Annex I of this report, and the completed reviews are summarized in Section A below.

In mid-2024, the JIU added a review of the ombudsman function and mediation services within United Nations entities to its work program. This review is part of the JIU’s series of reports on oversight, integrity, and accountability. With this review, the JIU completes its cycle of updating or supplementing previous reviews of the United Nations system that fall under this category of reports. Building on the findings of the 2015 review of ombudsman services in UN system organizations and complementing the 2023 review of internal pre-litigation grievance mechanisms, the ongoing review examines the current state of the function within entities and the evolution of its role in resolving disputes amicably and fostering a harmonious work environment. It assesses the effectiveness of the institutional framework, mandates, and key areas of responsibility of the function, as well as the implementation of recommendations from the previous report and any new developments impacting the function. Based on its findings, and with an emphasis on best practices, the review will formulate recommendations to enhance the coherence, efficiency, and effectiveness of the ombudsman function and mediation services. The results will be presented to the General Assembly under an agenda item at its eighty-first session.

Following the summaries of completed reports and notes in this chapter, the JIU provides an overview of other key activities undertaken in 2024, including dialogue with the heads of secretariats of participating entities, oversight bodies, deliberative bodies, and governing bodies. This chapter also includes the mid-term assessment of the JIU’s strategic framework and the follow-up on recommendations from its self-evaluation, along with an update on JIU resources and the measures taken to replace the system for tracking recommendations addressed to participating entities.




"""

original_bleu_score, original__meteor_score_value = calculate_scores(
    references, original)
grammar_bleu_score, grammar__meteor_score_value = calculate_scores(
    references, grammar)
accuracy_bleu_score, accuracy__meteor_score_value = calculate_scores(
    references, accuracy)
context_bleu_score, context__meteor_score_value = calculate_scores(
    references, context)
consistency_bleu_score, consistency__meteor_score_value = calculate_scores(
    references, consistency)
print(f"original BLEU Score: {original_bleu_score:.4f}")
print(f"original METEOR Score: {original__meteor_score_value:.4f}")
print(f"grammar BLEU Score: {grammar_bleu_score:.4f}")
print(f"grammar METEOR Score: {grammar__meteor_score_value:.4f}")
print(f"accuracy BLEU Score: {accuracy_bleu_score:.4f}")
print(f"accuracy METEOR Score: {accuracy__meteor_score_value:.4f}")
print(f"context BLEU Score: {context_bleu_score:.4f}")
print(f"context METEOR Score: {context__meteor_score_value:.4f}")
print(f"consistency BLEU Score: {consistency_bleu_score:.4f}")
print(f"consistency METEOR Score: {consistency__meteor_score_value:.4f}")
