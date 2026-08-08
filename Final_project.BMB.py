
# Capstone Project: Automated DNA Toolkit & Mutation Analyzer

# Global Dictionary Literal for Codon to Amino Acid mapping (Abbreviated)
CODON_MAP = {
    "AUG": "Methionine (START)", "UAA": "STOP", "UAG": "STOP", "UGA": "STOP",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine", "AAA": "Lysine"
}

print("=== MOLECULAR BIOLOGY TOOLKIT SYSTEM V1.0 ===")

running = True
while running:
    print("\n[MAIN MENU]")
    print("1. Analyze New DNA Sequence")
    print("2. Exit Toolkit")
    
    choice = input("Select an option (1-2): ")
    
    if choice == "2":
        print("Exiting toolkit. Happy researching!")
        running = False
        continue
        
    elif choice == "1":
        raw_dna = input("Enter or paste your DNA sequence: ").upper()
        
        # 1. Validation Logic
        is_valid = True
        for base in raw_dna:
            if base not in ["A", "T", "C", "G"]:
                is_valid = False
                break
                
        if not is_valid:
            print("Error: Invalid sequence detected! DNA must only contain A, T, C, G.")
            continue
            
        print(f"\nSequence accepted. Total bases: {len(raw_dna)}")
        
        # 2. Operators: Calculate GC Content
        gc_count = 0
        for base in raw_dna:
            if base == "G" or base == "C":
                gc_count += 1
        
        gc_percentage = (gc_count / len(raw_dna)) * 100
        print(f"Calculated GC Content: {gc_percentage:.2f}%")
        
        # 3. Transcription Phase (DNA -> mRNA)
        mrna = ""
        for base in raw_dna:
            if base == "T":
                mrna += "U"
            else:
                mrna += base
        print(f"Transcribed mRNA: {mrna}")
        
        # 4. Codon Parsing and Translation List
        codons_list = []
        # Loop steps by 3 to extract complete triplets
        for i in range(0, len(mrna) - (len(mrna) % 3), 3):
            triplet = mrna[i:i+3]
            codons_list.append(triplet)
            
        print(f"Isolated Codons List: {codons_list}")
        
        # 5. Mutation Detection Analysis
        stop_codon_found = False
        for index in range(len(codons_list)):
            current_codon = codons_list[index]
            if current_codon in ["UAA", "UAG", "UGA"]:
                print(f"WARNING: Premature STOP mutation discovered at codon index {index} ({current_codon})!")
                stop_codon_found = True
                
        if not stop_codon_found:
            print("No premature stop mutations detected in this reading frame.")
            
    else:
        print("Invalid choice. Please pick 1 or 2.")
