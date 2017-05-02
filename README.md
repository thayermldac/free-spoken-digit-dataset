# Forked Repo Introduction
I forked this dataset from the [original repo](https://github.com/Jakobovski/free-spoken-digit-dataset) in order to add utility functions and set it up for out-of-the-box use in training and testing machine learning models. 


Find below more details on the dataset from the parent repository. 

-----

## Free Spoken Digit Dataset (FSDD)

A simple audio/speech dataset consisting of recordings of spoken digits in `wav` files at **8kHz**. The recordings are trimmed so that they have near minimal silence at the beginnings and ends.

FSDD is an open dataset, which means it will grow overtime as data is contributed. Thus in order to enable reproducibility and accurate citation in scientific journals the dataset is versioned using `git tags`. 

### Current status
- 1 speakers
- 500 recordings (50 of each digit)
- English pronunciations

### Organization
Files are named in the following format:
`{digitLabel}_{speakerName}_{index}.wav`
Example: `7_jackson_32.wav`
