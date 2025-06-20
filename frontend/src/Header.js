import { Link } from "react-router-dom";
import styles from "./Header.module.css";

export default function Header() {
  return (
    <header>
      <nav className={styles.navigation}>
        <Link to="/"> Home </Link>
        <Link to="/history"> History </Link>
      </nav>
    </header>
  );
}
