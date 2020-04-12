using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DialogueManager : MonoBehaviour {

	public Text nameText;
	public Text dialogueText;

	public Animator animator;

	private Queue<string> sentences;

	private List<string> sentencesList;

	// Use this for initialization
	void Start () {
		sentences = new Queue<string>();
		sentencesList = new List<string>();
		
	}

	public void StartDialogue (Dialogue dialogue)
	{
		animator.SetBool("IsOpen", true);

		nameText.text = dialogue.name;

		sentences.Clear();

		foreach (string sentence in dialogue.sentences)
		{
			sentences.Enqueue(sentence);
			sentencesList.Add(sentence);
		}


		//DisplayNextSentence();
		DisplayNextSentence(0);
	}

	// public void DisplayNextSentence ()
	// {
	// 	if (sentences.Count == 0)
	// 	{
	// 		EndDialogue();
	// 		return;
	// 	}

	// 	string sentence = sentences.Dequeue();
	// 	Debug.Log(sentences);
	// 	StopAllCoroutines();
	// 	StartCoroutine(TypeSentence(sentence));
	// }

	public void DisplayNextSentence (int dialogNumber)
	{
		if (sentences.Count == 0)
		{
			EndDialogue();
			return;
		}
		string sentence = sentencesList[dialogNumber];
		//string sentence = sentences.Dequeue();
		//Debug.Log(sentences);
		StopAllCoroutines();
		StartCoroutine(TypeSentence(sentence));
	}

	IEnumerator TypeSentence (string sentence)
	{
		dialogueText.text = "";
		foreach (char letter in sentence.ToCharArray())
		{
			dialogueText.text += letter;
			yield return null;
		}
	}

	void EndDialogue()
	{
		animator.SetBool("IsOpen", false);
	}

}
