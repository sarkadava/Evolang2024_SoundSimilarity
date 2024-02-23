# Exploring the sound structure of novel vocalizations (Repository for paper submitted to Evolang XV)

# Folder structure

The repository contains RMarkdown with code to analyse sound similarity in novel vocalizations.

<pre>
├── data
├── datasets
└── plots
</pre>

This folder in the repository contains: 
1. <i>data</i> - file with duration of each segment (the original .wav files are not publicly available)
2. <i> datasets </i> - datasets that have been used to perform analysis and make plots 
        - distance_matrix: matrix of distances between a segment and all other segments
        - segments_soundgen_summary: ouput of soundgen() function
        - umap_df - dataset of concepts and their coordinates in reduced 2-dimensional space
        - meanDist_pertrial: complete dataset with all metadata, used features, plus mean calculated from 'distance_matrix' within a trial (i.e., concrete realization of a concept by a participant)
        - meanDist_perpcn: complete dataset with all metadata, used features, plus mean calculated from 'distance_matrix' within a participant (ignoring trial differentiation)
    3. <i>plots</i>
