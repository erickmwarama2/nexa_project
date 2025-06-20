import { useEffect, useState } from "react";
import { formatDate } from "./utils/utils";

export default function History() {
  const [questions, setQuestions] = useState([]);
  useEffect(() => {
    (async function () {
      try {
        const response = await fetch("http://localhost:8000/history");
        const data = await response.json();
        const questions = data.response;
        setQuestions(questions);
      } catch (error) {
        console.log(error);
      }
    })();
  }, []);

  return (
    <div>
      <ol>
        {questions.map((question) => (
          <li>
            {question.question} - Created at {formatDate(question.created_at)}
          </li>
        ))}
      </ol>
    </div>
  );
}
