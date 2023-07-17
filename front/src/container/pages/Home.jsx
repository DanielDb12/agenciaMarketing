import Layout from "../../hocs/layout/Layout";
import Footer from "../../components/navigation/Footer";
import Navbar from "../../components/navigation/Navbar";
import Header from "../../components/home/Header";
import Incentive from "../../components/home/Incentives";
import Cases from "../../components/home/Cases";
import Feature from "../../components/home/Feature";
import CTA from "../../components/home/CTA"
import LogoCloud from "../../components/home/LogoCloud"
import BlogList from "../../components/home/BlogList"

export const Home = () => {
  return (

    <Layout>
      <Navbar />
<div data-scroll-section className="pt-28">
      <Header />
      <Incentive />
	<Cases/>
	<Feature/>
	<CTA/>
	<LogoCloud/>
	<BlogList/>
     <Footer />
</div>
    </Layout>

  );
};
