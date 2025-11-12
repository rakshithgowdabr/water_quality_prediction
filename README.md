### water_quality_prediction

### Software And Tools REquirements

1. [github account](https://github.com)
2. [HerokuAccount](https://heroku.com)
3. [VScodeIDE](https://code.visualstudio.com/)

Getting-started-the-command-line

create a new environment

---
conda create -p venv python==3.7 -y
---

# Welcome to the Water Quality Dataset!
* In this dataset, we will analyze and predict water quality (specifically, whether it is drinkable or non-drinkable) using various metrics.

* It must be said, it is a great shame for humanity that in the 21st century, there are still people without access to clean water. Let’s hope this issue is resolved as soon as possible!

## A Quick Overview of the Data.

#### Water Quality Parameters Summary

1. **pH Value**:  
   pH indicates the acid-base balance of water. WHO recommends a pH range of 6.5 to 8.5. Current investigation shows values between 6.52 and 6.83, which are within this range.

2. **Hardness**:  
   Hardness is caused by dissolved calcium and magnesium salts, impacting water's ability to lather soap. It is determined by the contact time between water and geological deposits.

3. **Total Dissolved Solids (TDS)**:  
   TDS measures dissolved inorganic and organic minerals. A high TDS value indicates highly mineralized water. The desirable limit is 500 mg/L, with a maximum of 1000 mg/L for drinking purposes.

4. **Chloramines**:  
   Formed when ammonia is added to chlorine, chloramines disinfect water. Levels up to 4 mg/L are safe for drinking.

5. **Sulfate**:  
   Sulfates are naturally occurring and prevalent in soil and rocks. Concentrations in freshwater range from 3 to 30 mg/L, with some areas having higher levels up to 1000 mg/L.

6. **Conductivity**:  
   Electrical conductivity increases with the concentration of dissolved ions. WHO recommends a maximum conductivity of 400 μS/cm.

7. **Total Organic Carbon (TOC)**:  
   TOC measures carbon from organic compounds. For drinking water, TOC should be less than 2 mg/L, with source water having up to 4 mg/L.

8. **Trihalomethanes (THMs)**:  
   Formed during chlorine treatment, THMs should not exceed 80 ppm in drinking water.

9. **Turbidity**:  
   A measure of water clarity, affected by suspended solids. WHO recommends a turbidity value below 5 NTU, with 0.98 NTU observed in the study.

10. **Potability**:  
    Indicates if water is safe for consumption, where 1 means potable and 0 means not potable.


## What are We Going to Do?
* Data Preprocessing
* Missing Data Analysis
* Data Visualization
* Model Building with sklearn Library

# Conclusion

We can’t say we wrote the best code in the world, but we’ve definitely made progress. Much better results can be achieved with different models and approaches. If you have any experiments or feedback, I’m here and happy to assist. Stay healthy!