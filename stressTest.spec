/*
A KBase module: stressTest
*/

module stressTest {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_stressTest(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
    funcdef run_stressTest2(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
    funcdef run_stressTest3(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
