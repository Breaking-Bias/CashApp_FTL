import "./GuidancePage.css";

function GuidancePage() {
    return (
    <div className="guidance-container">
        <h2>Guidance on Using the Breaking Bias Application</h2>
    
        <p>Welcome to <strong>Breaking Bias</strong>! Below are some simple steps to help you get started:</p>
    
    <ul className="step-list">
        <li>
            <strong>Graph Overview:</strong> The graph on the main page displays the historical and predicted user base, along with transaction value changes resulting from the removal of bias.
        </li>
        <li>
            <strong>Variable Options:</strong> You can choose the gender variable (male, female, other) or select "no filter" for analysis.
        </li>
        <li>
            <strong>Prediction Size:</strong> Use the slider to adjust the prediction size, up to ** days.
        </li>
        <li>
            <strong>Need More Help?</strong> For additional assistance, reach out to our support team via email: <a href="mailto:mrbigboss@gmail.com">bigboss@gmail.com</a>.
        </li>
    </ul>
    </div>
    )
}

export default GuidancePage;

