from recommender.comparators.cpe_comparator import CpeComparator


class AntivirusComparator(CpeComparator):
    """
    Compares antivirus software between hosts.
    """
    
    def get_name(self):
        return "Antivirus"

    def calc_partial_similarity(self, host):
        """
        Calculates partial similarity of antivirus software running on
        compared hosts.
        :param host: Host object (host to be compared with reference host)
        :return: Partial similarity of antivirus software
        """

        partial_similarity, critical = self.compare_sw_components(
            self._reference_host.antivirus_component, host.antivirus_component)

        if critical:
            self._add_warning_message(host, "Similar antivirus between hosts.",
                                      partial_similarity)

        return partial_similarity
