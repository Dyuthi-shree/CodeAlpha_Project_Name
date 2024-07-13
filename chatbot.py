#question:answer
import time
now=time.ctime()


qna={
    "hi":"hey",
    
    "what is biotechnology":"it is a interbranch that deals with technological advacements to improve biological advacements ",
    "what is dna":"deoxyribose nuclic acid",
    "what is rna ":"ribose nuclic acid",
    "what is the time now":now,
    "crisper cas9":"It is a revolutionary technolgy for genetic engineering and biotechnology .it stands for clustered regularly interspaced short palindromic repeats ",
    "How it works":"GUIDE RNA:crisper cas9 uses guide RNA that matches the DNA sequence of interest.CAS9 ENZYME:The cas9  protien acts as molecular scissors that cuts the DNA at the targeted location.DNA REPAIR: once the DNA is cut ,the cells natural repair mechanisms kick in .This can lead  to the insertion or deletion of genetic material ,or the precise replacement of a DNA Sequence "
    
    
    
}
valid_questions = "\n".join([
    "hi",
    "what is biotechnology",
    "what is dna",
    "what is rna",
    "what is the time now",
    "crisper cas9",
    "how it works"
])
     
while True:
    qs = input("Ask a question: ").strip().lower()
    
    if qs == "quit":
        break
    elif qs in qna:
        print(qna[qs])
    else:
        print("Sorry, I don't understand that question. Please ask one of the following questions:")
        print(valid_questions)

    
    
    