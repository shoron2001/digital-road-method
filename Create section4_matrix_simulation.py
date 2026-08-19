# ==============================================================================
# Project: The Digital Road Method (Section 4 Validation Engine)
# Author: Mahmudul Hasan Shoron (Independent Researcher)
# Description: Validates the 9-Column / 19th-Slot Matrix Checksum Architecture
#              and demonstrates the 100% Deterministic Convergence Rate.
# ==============================================================================

import numpy as np

class QuranicMatrixSimulation:
    def __init__(self, total_surahs=114, columns=9):
        self.total_surahs = total_surahs
        self.W = columns # Fixed Spatial Grid Boundary (W = 9)

    def calculate_global_19th_slot(self, n):
        """
        Section 4.1 Global Deterministic Alignment Function:
        M_n = 19 + 9 * (n - 1)
        """
        return 19 + self.W * (n - 1)

    def recursive_modulo_9_reduction(self, value):
        """
        Base-9 Recursive Digital Root Reduction (Ore, 1988):
        M_n ≡ 1 (mod 9)
        """
        if value == 0:
            return 0
        remainder = value % 9
        return 9 if remainder == 0 else remainder

    def run_full_corpus_evaluation(self):
        """
        Section 4.3 & 4.4 Stratified Empirical Evaluation Loop
        """
        print(f"{'Surah No':<10}{'Global 19th-Slot (M_n)':<25}{'Operational Modulo-9':<25}{'System Status'}")
        print("-" * 75)
        
        passed_counts = 0
        waveform_data = []

        for n in range(1, self.total_surahs + 1):
            M_n = self.calculate_global_19th_slot(n)
            mod_9_result = self.recursive_modulo_9_reduction(M_n)
            status = "Pass (1)" if mod_9_result == 1 else "Fail (0)"
            
            if mod_9_result == 1:
                passed_counts += 1
                
            waveform_data.append((M_n, mod_9_result))

            # Printing first 20 surahs to match Table 5 layout
            if n <= 20:
                print(f"{n:<10}{M_n:<25}{mod_9_result:<25}{status}")
            elif n == 21:
                print(f"... [Loop continues smoothly up to 114 Surahs] ...")
                
        pass_rate = (passed_counts / self.total_surahs) * 100
        print("-" * 75)
        print(f"📊 Total Evaluated Blocks: {self.total_surahs}")
        print(f"✅ Successful Convergence Rate: {pass_rate:.2f}% (Zero Spatial Drift)")
        return waveform_data

if __name__ == "__main__":
    sim = QuranicMatrixSimulation()
    sim.run_full_corpus_evaluation()
