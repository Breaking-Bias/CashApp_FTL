import "./GuidancePage.css";

function GuidancePage() {
    return (
        <div>
            <h2> Guidance on using the Breaking Bias Application</h2>
            <p>Welcome to Breaking Bias! Here are some steps to help you get started:</p>
            <ol>
                <li>On the main page, the graph shows the historical and predicted user base and transaction value jump due to the underlying bias removed </li>
                <li>Options for variables includes: Gender - male, female, other and no filter</li>
                <li>The prediction size could be adjusted with the slider - up to ** days</li>
            </ol>
        </div>
    )
}

export default GuidancePage;

