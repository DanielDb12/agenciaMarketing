import { connect } from "react-redux";
import img_logo from "../../assets/img/logo.png";
import React from "react";
import { Link } from "react-router-dom";
import loader from "../../assets/img/loader.gif";

export const Navbar = () => {
  return (
    <nav className="w-full py-2 bg-white  sticky top-0  ">
      <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
        <a href="https://flowbite.com/" className="flex items-center">
          <img src={img_logo} className="h-10 mr-3" alt="Flowbite Logo" />
          <span className="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">
            DIGITAL AGENCY
          </span>
        </a>
        <button
          data-collapse-toggle="navbar-default"
          type="button"
          className="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
          aria-controls="navbar-default"
          aria-expanded="false"
        >
          <span className="sr-only">Open main menu</span>
        </button>

        <div className="hidden w-full md:block md:w-auto" id="navbar-default">
          <ul className="font-medium flex items-center flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
            <Link
              to="#"
              className="block py-2 pl-3 pr-4 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 dark:text-white md:dark:text-blue-500"
              aria-current="page"
            >
              Home
            </Link>
            <Link
              to="/casos"
              className=" rounded-none block py-2 pl-3 pr-4 text-gray-900  border-b-2  transition duration-300 ease-in-out hover:bg-gray-100 md:hover:bg-transparent md:border-white md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
            >
              <span className="link link-underline link-underline-black text-black">
                {" "}
                Casos{" "}
              </span>
            </Link>
            <Link
              to="servicios"
              className="  block py-2 pl-3 pr-4 text-gray-900    hover:bg-gray-100 md:hover:bg-transparent  md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
            >
              <span className="link link-underline link-underline-black text-black">
                Servicios
              </span>
            </Link>
            <Link
              to="/nosotros"
              className="block py-2 pl-3 pr-4 text-gray-900  hover:bg-gray-100 md:hover:bg-transparent md:border-white  hover:border-blue-800 after:opacity-0 after:transform md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
            >
              <span className="link link-underline link-underline-black text-black">
                Nosotros
              </span>
            </Link>
            <Link
              to="carreras"
              className="  block py-2 pl-3 pr-4 text-gray-900    hover:bg-gray-100 md:hover:bg-transparent  md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
            >
              <span className="link link-underline link-underline-black text-black">
                Carreras
              </span>
            </Link>
            <Link
              to="/blog"
              className="  block py-2 pl-3 pr-4 text-gray-900    hover:bg-gray-100 md:hover:bg-transparent  md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
            >
              <span className="link link-underline link-underline-black text-black">
                Blog
              </span>
            </Link>
            <Link
              to="/contacto"
              className="  block py-2 pl-3 pr-4 text-gray-900    hover:bg-gray-100 md:hover:bg-transparent  md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
            >
              <span className="link link-underline link-underline-black text-black">
                Contacto
              </span>
            </Link>
            <button
              type="button"
              className="  transition duration-300 text-white bg-gradient-to-r from-cyan-500 to-blue-500 hover:bg-gradient-to-bl hover:opacity-80  ease-in-out  focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 font-medium rounded-lg text-sm px-8 py-2.5 text-center mr-2 mb-2"
            >
              <span className="flex items-center ">
                Cv
                <img
                  className="px-2"
                  width={40}
                  height={40}
                  src={loader}
                  alt=""
                ></img>{" "}
              </span>
            </button>
          </ul>
        </div>
      </div>
    </nav>
  );
};

const mapStateToProps = (state) => ({});

export default connect(mapStateToProps, {})(Navbar);
