# Breaking Bias x Cash App x FTL

Bias Visualization & Prediction Tool (BVPT)

Frontend hosted with Netlify [here](https://superlative-entremet-ffedcc.netlify.app)

Backend hosted with DigitalOcean [here](https://breakingbiasbigboss.zapto.org/)

# Project Overview

Bias is everywhere. People, organizations, media outlets, and yes, even machine learning models can be biased. We at Breaking Bias are focused on tackling the latter, to ensure that no groups are unjustly affected by hidden ML bias. We have developed the Bias Visualization and Prediction Tool (BVPT), a project designed to help non-technical decision makers at Cash App visualize the impact that ML bias has on their bottom line in the short-to-long term.

Our project focuses on two metrics: cash flow and transaction volume. Given a dataset of transactions over a period of time, with some transactions explicitly labelled as biased, the BVPT displays the orginial dataset, along with an unbiased version of the dataset (note that transactions flagged as biased do not count toward the total, since they are halted before the transaction is completed. This means that there is a greater number of total transactions in the unbiased dataset).

The graph displays how cash flow and transaction volume fluctuate over this period for both the biased and unbiased datasets, and makes a prediction for how each of these may evolve in the future. This prediction is done via an Autoregressive Integrated Moving Average (ARIMA) Model. For more information about this, check out our project files and read this [article on the ARIMA model](https://www.investopedia.com/terms/a/autoregressive-integrated-moving-average-arima.asp).

# Usage

Initially, you will be prompted to upload a dataset. This is optional as there is already a trial dataset loaded.
Click Start, read through the "How to Use the App" prompt, press Close, and you are ready to get started.

There are many ways to customize what you want the graph for display. The following are the available options.

| Metrics                                | Prediction Size        | Filters                    |
| -------------------------------------- | ---------------------- | -------------------------- |
| - Cash Flow <br/> - Transaction Volume | - Slider (10-100 days) | - Gender <br/> - Ethnicity |

# Running the Project

### Requirements:

- Git
- Node.js
- Python

### To run the front end:

```
cd frontend
npm install
npm run dev
```

### To run the back end:

```
cd backend
pip install -r requirements.txt
python server.py (or click the play button)
```

# Backend File Structure

```
backend/
├── app/
│   └── app.py
├── data_access/
│   ├── data_access_object.py
│   └── file_uploader.py
├── entity/
│   ├── difference_calculator.py
│   ├── filters.py
│   ├── graphing_data.py
│   └── model.py
├── interface_adaptor/
│   ├── prediction/
│   │   └── prediction_controller.py
│   ├── upload_file/
│   │   └── upload_file_controller.py
│   └── view_result/
│       └── view_result_controller.py
├── use_case/
│   ├── interactor_helpers/
│   │   ├── data_factory.py
│   │   ├── data_formatter.py
│   │   ├── filter_interactor.py
│   │   ├── graph_adapter.py
│   │   └── model_interactor.py
│   ├── prediction/
│   │   └── prediction_interactor.py
│   ├── upload_file/
│   │   └── upload_file_interactor.py
│   ├── view_result/
│   │   └── view_result_interactor.py
```

# Contributors

- @Adventurer-E
- @avantitandon
- @BardyBard
- @MatthewFrieri
- @solarescarlos
- @taheat04

# Acknowledgments

Special thanks to all contributors, mentors, and collaborators who made this project possible.

# License

This project is licensed under the MIT License
