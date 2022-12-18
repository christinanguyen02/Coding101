import React from "react";
import "./about.css";
import { Carousel, Row } from "react-bootstrap";
import pic1 from "../gallery1.jpg";
import pic2 from "../gallery2.jpg";
import pic3 from "../gallery3.jpg";
import pic4 from "../gallery4.jpg";
import pic5 from "../gallery5.jpg";
import pic6 from "../gallery6.jpg";
import kuromi from "../aboutKuromi.png";

export default function About() {
  return (
    <div className="main">
      <div>
        <Row className="aboutIntro">
          <p className="aboutText">
            {" "}
            About Me!&nbsp;&nbsp;
            <img className="Kuropic" src={kuromi} alt="Kuromi"></img>
          </p>
        </Row>
        <Row className="description">
          <p>
            Hi, I'm Christina Nguyen. I am a current student at the University
            of Texas at Austin. I am currently pursuing a Bachelor of Science in
            Biochemistry with an Elements of Computing certificate.
            <br></br>
          </p>
          <p>
            I am currently working as a Course Grader for the University of
            Texas OnRamps program. Also, I volunteer at the Baylor Scott and
            White Medical Center in Austin. Furthermore, I just crossed into
            Sigma Phi Omega, an asian-interest sorority at the University of
            Texas at Austin. If you're interested about learning more about my
            sorority check out our{" "}
            <a href="https://www.txsigmas.com/">website</a> or our
            <a href="https://linktr.ee/texassigmas"> linktree</a>.<br></br>
          </p>
          <p>
            In my free time, I like to code and work on projects, read, watch
            k-dramas and anime, workout, play tennis, and bullet journal. Also,
            I really like Kuromi from Sanrio!
          </p>
        </Row>
      </div>
      <div id="myCarousel" class="carouselslide">
        <Row className="carousel">
          <div class="carousel-inner">
            <Carousel variant="dark">
              <Carousel.Item>
                <img className="d-block w-100" src={pic6} alt="First slide" />
              </Carousel.Item>
              <Carousel.Item>
                <img className="d-block w-100" src={pic5} alt="Second slide" />
              </Carousel.Item>
              <Carousel.Item>
                <img className="d-block w-100" src={pic4} alt="Third slide" />
              </Carousel.Item>
              <Carousel.Item>
                <img className="d-block w-100" src={pic3} alt="Fourth slide" />
              </Carousel.Item>
              <Carousel.Item>
                <img className="d-block w-100" src={pic2} alt="Fifth slide" />
              </Carousel.Item>
              <Carousel.Item>
                <img className="d-block w-100" src={pic1} alt="Sixth slide" />
              </Carousel.Item>
            </Carousel>
          </div>
        </Row>
      </div>
    </div>
  );
}
