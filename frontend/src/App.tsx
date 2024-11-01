import "./App.css";
import Graph from "./components/Graph";
import Button from './components/Button';

function App() {
  const serverURL = import.meta.env.VITE_SERVER_URL;

  async function makeTestGetRequest() {
    const endpoint = serverURL + "/getinfo";

    try {
      // make the request
      const response = await fetch(endpoint);

      // catch errors in fetch response
      if (!response.ok) {
        throw new Error("Error in response:" + response.statusText);
      }

      // convert the data to json
      const data = await response.json();

      console.log(data);
    } catch (error) {
      console.error("Error:", error);
    }
  }

  return (
    <>
      <h1>This is our front end</h1>
      <button onClick={makeTestGetRequest}>
        Click me to get some info from the back end
      </button>
      <div style={{ display: 'flex', gap: '10px'}}>
        <Button label="Age" backgroundColor="green" fontSize={14} />
        <Button label="Gender" backgroundColor="green" fontSize={14} />
        <Button label="Race" backgroundColor="green" fontSize={14} />
        <Button label="Location" backgroundColor="green" fontSize={14} />
      </div>

      <Graph />
    </>
  );
}

export default App;
