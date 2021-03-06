import streamlit as st

def app():
    st.title("Description")
    st.header("[Predicting Alzheimer’s disease progression trajectory and clinical subtypes using machine learning](https://www.biorxiv.org/content/10.1101/792432v2)")
    
    
    st.write("## Summary")
    st.write("### Background")
    st.write("Alzheimer’s disease (AD) is a common, age-related, neurodegenerative disease that impairs a person’s ability to perform day-to-day activities. Diagnosing AD is challenging, especially in the early stages. Many patients still go undiagnosed, partly due to the complex heterogeneity in disease progression. This highlights a need for early prediction of the disease course to assist its treatment and tailor therapy options to the disease progression rate. Recent developments in machine learning techniques provide the potential to not only predict disease progression and trajectory of AD but also to classify the disease into different etiological subtypes.")
    st.write("### Methods")
    st.write("The work shown here clusters participants in distinct and multifaceted progression subgroups of AD and discusses an approach to predict the progression rate from baseline diagnosis. We observed that the myriad of clinically reported symptoms summarized in the proposed AD progression space corresponds directly with memory and cognitive measures, which are routinely used to monitor disease onset and progression. Our analysis demonstrated accurate prediction of disease progression after four years from the first 12 months of post-diagnosis clinical data (Area Under the Curve of 0.96 (95% confidence interval (CI), 0.92-1.0), 0.81 (95% CI, 0.74-0.88) and 0.98 (95% CI, 0.96-1.0) for slow, moderate and fast progression rate patients respectively). Further, we explored the long short-term memory (LSTM) neural networks to predict the trajectory of an individual patient’s progression.")
    # st.write("We applied machine learning algorithms to a prospective, population-based cohort consisting of 2,858 Italian patients diagnosed with ALS for whom detailed clinical phenotype data were available. We replicated our findings in an independent population-based cohort of 1,097 Italian ALS patients.")
    st.write("### Conclusion")
    st.write("The machine learning techniques presented in this study may assist providers in identifying different progression rates and trajectories in the early stages of the disease, hence allowing for more efficient and personalized healthcare deliveries. With additional information about the progression rate of AD at hand, providers may further individualize the treatment plans. The predictive tests discussed in this study not only allow for early AD diagnosis but also facilitate the characterization of distinct AD subtypes relating to trajectories of disease progression. These findings are a crucial step forward for early disease detection. These models can be used to design improved clinical trials for AD research.")
