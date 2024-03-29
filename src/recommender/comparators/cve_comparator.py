from recommender.comparators.cumulative_comparator \
    import CumulativeSimilarityComparator


class CveComparator(CumulativeSimilarityComparator):
    """
    Compares the history of CVEs.
    """

    def __init__(self, config, total_cve_count):
        super().__init__(config)
        self.total_cve_count = total_cve_count

    def get_name(self):
        return "CVE"

    def calc_partial_similarity(self, host):
        """
        Calculates cumulative similarity of the number of vulnerabilities (CVE)
        on hosts
        :param host: Host object (host to be compared with reference host)
        :return: Cumulative partial similarity
        """

        partial_similarity, critical = self._calculate_cumulative_similarity(
            self._reference_host.cve_count,
            host.cve_count,
            self.total_cve_count)

        if critical:
            self._add_warning_message(host,
                                      "High cumulative vulnerability count.",
                                      partial_similarity)

        return partial_similarity
