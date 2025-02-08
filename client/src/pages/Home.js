import React from "react";

const Home = () => {
  const handleButtonClick = (college) => {
    alert(`You selected ${college}`);
    // You can add more functionality here, like routing or redirecting.
  };

  return (
    <div>
      <h1>Welcome to CourseMap</h1>
      <button onClick={() => handleButtonClick("Columbia")}>
        Go to Columbia
      </button>
      <button onClick={() => handleButtonClick("Queens College")}>
        Go to Queens College
      </button>
    </div>
  );
};

export default Home;
