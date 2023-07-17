import Layout from "../../hocs/layout/Layout";
import Footer from "../../components/navigation/Footer";
import Navbar from "../../components/navigation/Navbar";
import CasesList from "../../components/cases/CasesList";
import React from "react";

export const Cases = () => {
  return (

    <Layout>
      <Navbar />
 <div className="pt-28">
      <CasesList/>
      <Footer />
</div>
    </Layout>

  );
};
