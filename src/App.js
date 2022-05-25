import { Container, Row, Col } from "react-bootstrap";
import Christina from "./christina.jpeg";
import "./App.css";
import home from "./homekuromi.png";

function App() {
  return (
    <>
      <div className="App">
        <Container fluid>
          <Row className="spacing">
            <Col>
              {" "}
              <img src={Christina} className="Main-photo" alt="" />
              <p className="caption">
                Picture taken at Japanese Tea Garden.
              </p>{" "}
            </Col>
            <Col className="Intro">
              <p className="Body">
                Hi! :) <br></br>Welcome to my website! <br></br>I'm Christina
                Nguyen! <br></br>
                <img src={home} className="kurohome" alt="home" />
              </p>
            </Col>
          </Row>
        </Container>
      </div>
    </>
  );
}

export default App;
