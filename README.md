## Language-Agnostic Bias Detection in Language Models with Bias Probing

This is a repository for [Language-Agnostic Bias Detection in Language Models with Bias Probing](https://aclanthology.org/2023.findings-emnlp.848/) at EMNLP 2023.

## 1. Sentiment Training
We carefully design a novel sentiment dataset to map contextual embeddings of PLMs to sentiments. Therefore, we propose a template-based approach with careful design. We select six languages
with diverse linguistic features based on the linguistic capabilities of the authors and conduct experiments in those languages: Arabic, Dutch, English,
French, German, and Turkish. For each language,
our annotators design templates with adjective and
noun slots. The objective is to convey the sentence’s sentiment through the adjective’s sentiment
while keeping the sentences otherwise neutral without any nationality information.

Training Dataset:

| Language | URL |
|----------|-----|
| Arabic   | [TRAIN-AR](https://github.com/akoksal/LABDet/blob/main/train/ar.json) |
| Dutch    | [TRAIN-NL](https://github.com/akoksal/LABDet/blob/main/train/nl.json) |
| English  | [TRAIN-EN](https://github.com/akoksal/LABDet/blob/main/train/en.json) |
| French   | [TRAIN-FR](https://github.com/akoksal/LABDet/blob/main/train/fr.json) |
| German   | [TRAIN-DE](https://github.com/akoksal/LABDet/blob/main/train/de.json) |
| Turkish  | [TRAIN-TR](https://github.com/akoksal/LABDet/blob/main/train/tr.json) |

Otherwise, you can create these files by using [train_dataset_generator.py](https://github.com/akoksal/LABDet/blob/main/train_dataset_generator.py).

## 2. Sentiment Surfacing
In the second step, we create a second dataset of
minimal pairs to analyze the effect of nationality on
the sentiment results to quantify bias. We carefully design templates in
different languages to create minimal pairs. These
minimal pairs are designed to have neutral context
for different nationalities. Our annotators create
templates with [Nationality] and [Adjective] tags
and this time they propose a neutral set of adjectives. Therefore, we aim to investigate the effect of
nationality change for positive/negative sentiment
surfacing.

Sentiment Surfacing Dataset:

| Language | URL |
|----------|-----|
| Arabic   | [Test-AR](https://github.com/akoksal/LABDet/blob/main/test/ar.json) |
| Dutch    | [Test-NL](https://github.com/akoksal/LABDet/blob/main/test/nl.json) |
| English  | [Test-EN](https://github.com/akoksal/LABDet/blob/main/test/en.json) |
| French   | [Test-FR](https://github.com/akoksal/LABDet/blob/main/test/fr.json) |
| German   | [TEST-DE](https://github.com/akoksal/LABDet/blob/main/test/de.json) |
| Turkish  | [TEST-TR](https://github.com/akoksal/LABDet/blob/main/test/tr.json) |

Otherwise, you can create these files by using [test_dataset_generator.py](https://github.com/akoksal/LABDet/blob/main/test_dataset_generator.py).


## Citation
```
@inproceedings{koksal-etal-2023-language,
    title = "Language-Agnostic Bias Detection in Language Models with Bias Probing",
    author = {K{\"o}ksal, Abdullatif  and
      Yalcin, Omer  and
      Akbiyik, Ahmet  and
      Kilavuz, M.  and
      Korhonen, Anna  and
      Schuetze, Hinrich},
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2023",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-emnlp.848",
    doi = "10.18653/v1/2023.findings-emnlp.848",
    pages = "12735--12747",
    abstract = "Pretrained language models (PLMs) are key components in NLP, but they contain strong social biases. Quantifying these biases is challenging because current methods focusing on fill-the-mask objectives are sensitive to slight changes in input. To address this, we propose a bias probing technique called LABDet, for evaluating social bias in PLMs with a robust and language-agnostic method. For nationality as a case study, we show that LABDet {``}surfaces{''} nationality bias by training a classifier on top of a frozen PLM on non-nationality sentiment detection. We find consistent patterns of nationality bias across monolingual PLMs in six languages that align with historical and political context. We also show for English BERT that bias surfaced by LABDet correlates well with bias in the pretraining data; thus, our work is one of the few studies that directly links pretraining data to PLM behavior. Finally, we verify LABDet{'}s reliability and applicability to different templates and languages through an extensive set of robustness checks. We publicly share our code and dataset in https://github.com/akoksal/LABDet.",
}
```
