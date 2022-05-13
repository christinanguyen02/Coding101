import { Container, Row, Col } from "react-bootstrap";
import Kuromi from "./Kuromi.png";
import "./App.css";

function App() {
  return (
    <>
      <div className="App">
        <header className="App-header">
          <Container fluid>
            <Row>
              <Col>
                {" "}
                <img src={Kuromi} className="App-logo" alt="logo" />
                <p>
                  Edit <code>src/App.js</code> ajajjajajaj.
                </p>{" "}
              </Col>
              <Col>
                <a
                  className="App-link"
                  href="https://reactjs.org"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Learn React
                </a>
              </Col>
            </Row>
          </Container>
        </header>
      </div>
    </>
  );
}

export default App;
