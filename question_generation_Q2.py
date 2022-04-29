import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForQuestionAnswering
import spacy


# qg_tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-question-generation-ap")
# qg_model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-question-generation-ap")

qg_tokenizer = AutoTokenizer.from_pretrained("bigscience/T0_3B")
qg_model = AutoModelForSeq2SeqLM.from_pretrained("bigscience/T0_3B")

nlp = spacy.load("en_core_web_sm")


def get_answer_candidates(text):
    doc = nlp(text)
    candidates = [ent.text for ent in list(doc.ents)]
    noun_chunks = list(doc.noun_chunks)
    for chunk in noun_chunks:
        found = False
        for cand in candidates:
            if chunk.text.lower() == cand.lower():
                found = True
        if not found:
            candidates.append(chunk.text)
    # candidates += [chunk.text for chunk in list(doc.noun_chunks) if chunk.text not in candidates]
    candidates = [cand for cand in candidates if cand.lower() != 'i']
    return candidates


def get_questions_beam(answer, context, max_length=128, beam_size=5, num_return=5):
    all_questions = []
    input_text = "answer: %s  context: %s </s>" % (answer, context)
    features = qg_tokenizer([input_text], return_tensors='pt')

    beam_outputs = qg_model.generate(input_ids=features['input_ids'], attention_mask=features['attention_mask'],
                                     max_length=max_length, num_beams=beam_size, no_repeat_ngram_size=3,
                                     num_return_sequences=num_return, early_stopping=True)

    for beam_output in beam_outputs:
        all_questions.append(qg_tokenizer.decode(beam_output, skip_special_tokens=True).replace("question: ", "", 1))

    return all_questions
